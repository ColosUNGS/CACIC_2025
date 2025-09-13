#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>
#include <omp.h>

int main(int argc, char* argv[]) {
    int myrank, numprocs, n, i;
    double starttime, endtime;
    double PI25DT = 3.141592653589793238462643;
    double h, x, local_sum = 0.0, total_sum = 0.0, pi;
    int threads_per_process;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
	MPI_Comm_size(MPI_COMM_WORLD, &numprocs);

	starttime = MPI_Wtime();
	
    if (myrank == 0) {
        FILE* in = fopen("pi_n.dat", "r");
        if (in == NULL) {
            perror("pi_n.dat");
            MPI_Abort(MPI_COMM_WORLD, 1);
        }
        fscanf(in, "%d", &n);
        fclose(in);
    }

    
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    h = 1.0 / (double)n;

    
    int start = myrank * (n / numprocs);
    int end = (myrank == numprocs - 1) ? n : start + (n / numprocs);

   
    #pragma omp parallel
    {
        double thread_sum = 0.0;
        #pragma omp for
        for (i = start; i < end; i++) {
            x = (i + 0.5) * h;
            thread_sum += 4.0 / (1.0 + x * x);
        }
        #pragma omp atomic
        local_sum += thread_sum;
    }

    
    MPI_Reduce(&local_sum, &total_sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    if (myrank == 0) {
        pi = h * total_sum;
        endtime = MPI_Wtime();  
		printf("Valor aproximado de pi %.16f, Error %.16f\n", pi, fabs(pi-PI25DT));
		printf("Tiempo = %f\n", endtime-starttime);
    }

    MPI_Finalize();
    return 0;
}
