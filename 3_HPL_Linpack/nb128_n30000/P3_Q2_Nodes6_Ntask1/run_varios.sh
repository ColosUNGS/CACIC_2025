for i in {1..5}; do
    JOB_NAME="nb128_n3k_6nodes_$i"
    sbatch --job-name="$JOB_NAME" runhpl.sh
    sleep 60m
done