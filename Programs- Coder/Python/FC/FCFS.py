
'''
    FCFS scheduler to calculate the average waiting time for each process.

    args:
        process_list: list of tuples representing each process.
        First value of the pair represents the arrival time of the process, while the second
        value represents the burst time, meaning the execution time of the process
'''
class FCFS:

    def __init__(self, process_list):
        self.n_process = len(process_list)

        # Sort process list by the arrival times
        self.process_list = sorted(process_list, key=lambda process: process[0])

        # Fetch arrival and burst time of each process at the same index
        self.arrival_time = [process[0] for process in self.process_list]
        self.burst_time = [process[1] for process in self.process_list]


    '''
    Calculate waiting time for each process, assuming the waiting time for the initial process is 0.
    '''
    def __calculate_waiting_times(self):

        # Initialize the waiting time list for each process with a 0 to aggregate later
        waiting_time = [0]*self.n_process

        # Skip the index 0, as the waiting time for the initial process at process_list[0] is assumed to be 0
        for idx in range(1,self.n_process):
            # Keep indexes of the previous and the current processes
            prev = idx-1
            curr = idx

            # Waiting time of the process with current idx will be from the arrival of the current process until the
            # end of the process
            end_of_previous_process = waiting_time[prev] + self.arrival_time[prev] + self.burst_time[prev]
            curr_waiting_time = end_of_previous_process - self.arrival_time[curr]

            # If waiting time is a positive number, meaning the process arrived while the previous process is still
            # running, assign value
            waiting_time[idx] = curr_waiting_time if curr_waiting_time > 0 else 0

        return waiting_time

    '''
    Calculate average waiting time for the whole process queue
    '''
    def calculate_average_waiting_time(self):

        # List of waiting times per each process
        waiting_times = self.__calculate_waiting_times()

        # Average waiting time
        return sum(waiting_times)/self.n_process


if __name__ == '__main__':

    # Example:
    #
    # Here we are trying to solve the FCFS scheduling problem to find the average waiting time of 3 processes
    # Process       Arrival time        Burst Time
    # p1             1                   3
    # p2             2                   4
    # p3             5                   1
    #
    # p1 will arrive at t=1 and end at t=1+3=4
    # p2 will arrive at t=2 and start at t=4 thus wait for t=2. It will end at t=4+4=8
    # p3 will arrive at t=5 and start at t=8, thus wait for t=3.
    #
    # The average waiting time is (3+2)/3=1.66

    processes =[(1,3),(2,4),(5,1)]

    fSolver = FCFS(processes)

    print(fSolver.calculate_average_waiting_time())
