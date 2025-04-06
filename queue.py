from collections import deque

#Queue class created.
class TicketQueue:
    def __init__(self):
        #Using deque for efficient queue operations
        self.queue = deque()

    def join_line(self, person):
        #For any Person that gets into the line. 
        print(f"{person} has joined the line.")
        self.queue.append(person)

    def serve_person(self):
        #Serves the person at the front of the line.
        if self.is_empty():
        #if no one is in line this message would appear.
            print("No one is in line.")
        else:
            served = self.queue.popleft()
            print(f"{served} has bought a concert ticket and left the line.")

    def is_empty(self):
        #Checks if the Queue is empty.
        return len(self.queue) == 0

    def show_line(self):
        # Display current state of the queue
        print("Current line:", list(self.queue))

#Usage Example:

# Create a ticket queue
line = TicketQueue()

#For the people who are joining the line in order.
#The people will get taken care in order of their line position.
line.join_line("Bob")
line.join_line("Sammy")
line.join_line("Kyle")

#Shows who is in line currently.
line.show_line()

# Serving people
line.serve_person() #Bob is in line 1st
line.serve_person()  #Sammy is in line next

#Shows current line again
line.show_line()

# Someone else joins the line
line.join_line("Diana")

# Serve the rest
line.show_line()
line.serve_person()  #Jyle gets served
line.serve_person()  #Diana gets served
line.serve_person()  # Line is empty now