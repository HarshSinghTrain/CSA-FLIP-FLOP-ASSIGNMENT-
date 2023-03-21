CODE:SR FIPL-FLOP:-

# initialize inputs and outputs
s = 0
r = 0
q = 0
q_bar = 0

# define function for SR flip-flop
def sr_flip_flop(s, r):
    global q, q_bar
    if s == 1 and r == 0:
        q = 1
        q_bar = 0
        print("Q is Set to 1 and Q_bar is reset to 0")
    elif s == 0 and r == 1:
        q = 0
        q_bar = 1
        print("Q_bar is Set to 1 and Q is reset to 0")
    elif s == 0 and r == 0:
        pass # no change
        print("No change hold condition")
    else: # s == 1 and r == 1
        print("Invalid input: s and r cannot be both 1")

# test the function with different inputs
S=int(input("Enter the value of S: "))
R=int(input("Enter the value of R: "))
sr_flip_flop(S, R)
if(S==0 and R==0):
    print("q =", q, "q_bar =", q_bar)
elif(S==1 and R==0):
    print("q =", q, "q_bar =", q_bar)
elif(S==0 and R==1):
    print("q =", q, "q_bar =", q_bar)
elif(S==1 and R==1): # this will print an error message
    print("")

CODE:JK FLIP-FLOP:-

# Initialize the J and K inputs
J = 0
K = 0

# Initialize the flip flop output and state
output = 0
state = 0

# Define the flip flop function
def jk_flip_flop(J, K, state):
    if J == 1 and K == 1:
        # Toggle the flip flop state
        if state == 0:
            state = 1
        else:
            state = 0
    elif J == 1:
        # Set the flip flop state to 1
        state = 1
    elif K == 1:
        # Set the flip flop state to 0
        state = 0
    # Output the flip flop state
    return state

# Test the flip flop function with various inputs
output = jk_flip_flop(0, 0, output)
print("Output: ", output)  # Output: 0

output = jk_flip_flop(1, 0, output)
print("Output: ", output)  # Output: 1

output = jk_flip_flop(0, 1, output)
print("Output: ", output)  # Output: 0

output = jk_flip_flop(1, 1, output)
print("Output: ", output)  # Output: 1

output = jk_flip_flop(1, 1, output)
print("Output: ", output)  # Output: 0
