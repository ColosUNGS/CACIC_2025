for i in {1..3}; do
    JOB_NAME="nb224_n3k_6nodes_$i"
    sbatch --job-name="$JOB_NAME" runhpl.sh
done