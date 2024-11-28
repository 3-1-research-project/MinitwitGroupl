import multiprocessing

bind = "0.0.0.0:5000"
loglevel = 'error'
preload = True # If true can save some RAM
reuse_port = False
daemon = False

# The range 2-4 x $(NUM_CORES) should be able to handle thousands of requests
workers = multiprocessing.cpu_count() * 2
# I Don't believe the MiniTwit appliation has too many blocking calls
worker_class = 'uvicorn.workers.UvicornWorker'
# A positive integer generally in the 2-4 x $(NUM_CORES) range
threads = multiprocessing.cpu_count() * 2
# max amount of simultaneous clients
worker_connections = 1000 

# amount of requests before restarting 0 means never restart
max_requests = 0 
# The jitter causes the restart per worker to be randomized by randint(0, max_requests_jitter). This is intended to stagger worker restarts to avoid all workers restarting at the same time.
max_requests_jitter = 0 

timeout = 120
# After receiving a restart signal, workers have this much time to finish serving requests.
graceful_timeout = 120 

# Generally set in the 1-5 seconds range for servers with direct connection to the client
# Note sync worker does not support persistent connections and will ignore this option.
# keepalive = 3