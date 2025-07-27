#include <stdio.h>
#include <float.h>
#include <math.h>
#include <mpi.h>

int main(int argc, char* argv[]) {
  int    myrank, numprocs;
  double starttime, endtime;
  int    i, n;
  double PI25DT = 3.141592653589793238462643;
  double x, sum=0.0, npi,pi, sum_acum=0.0,h;
  FILE*  in;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
  MPI_Comm_size(MPI_COMM_WORLD, &numprocs);

  starttime = MPI_Wtime();
  
  if ( myrank == 0 )
  {
	if ( (in = fopen("pi_n.dat", "r")) == NULL ) {
		perror("pi_n.dat");
		return 1;		
	}
	fscanf(in, "%d", &n);  
	fclose(in);	
  } 	
    
  MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
  h=1.0/(double)n;

  for (i=myrank+1; i<n; i+=numprocs) {
    x = (i + 0.5) * h;
    sum += 4.0 / ( 1.0 + x*x );
  }
  
  MPI_Reduce(&sum, &sum_acum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD); 
  
  if ( myrank == 0 ) {
	pi=h*sum_acum;
	endtime = MPI_Wtime();  
    	printf("Valor aproximado de pi %.16f, Error %.16f\n", pi, fabs(pi-PI25DT));
	printf("Tiempo = %f\n", endtime-starttime);
  } 
  MPI_Finalize(); 
  return 0;
}
