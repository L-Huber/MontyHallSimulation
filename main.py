import random

def configure_simulation():
    # you can configure the simulation here:
    # you can pick door 1,2,3
    picked_door=1
    # you can use the mode "stay" if you want to keep your choice
    # or you can choose "change" if you want to change your choice after the door is opened
    mode="stay"
    # you can difine, how many rounds should be simulated
    rounds = 1000
    simulation_round(picked_door,mode,rounds)
def simulation_round(picked_door,mode,rounds):
    correct = 0
    times_door_1_was_correct = 0
    times_door_2_was_correct = 0
    times_door_3_was_correct = 0
    for i in range(rounds):

        doors = [1, 2, 3]
        correct_door = random.choice(doors)

        if correct_door == 1:
            times_door_1_was_correct = times_door_1_was_correct+1
        if correct_door == 2:
            times_door_2_was_correct = times_door_2_was_correct + 1
        if correct_door == 3:
            times_door_3_was_correct = times_door_3_was_correct+1


        if picked_door == 1:
            if correct_door == 1:
                possible_doors =[2, 3]
                open_door = random.choice(possible_doors)
                if mode == "stay":
                    correct = correct+1
                else:
                    pass
            if correct_door == 2:
                open_door = 3
                if mode == "change":
                    correct = correct+1
                else:
                    pass
            if correct_door == 3:
                open_door = 2
                if mode == "change":
                    correct = correct+1
        if picked_door == 2:
            if correct_door == 2:
                possible_doors =[1, 3]
                open_door = random.choice(possible_doors)
                if mode == "stay":
                    correct = correct+1
                else:
                    pass
            if correct_door == 1:
                open_door = 3
                if mode == "change":
                    correct = correct+1
                else:
                    pass
            if correct_door == 3:
                open_door = 1
                if mode == "change":
                    correct = correct+1
        if picked_door == 3:
            if correct_door == 3:
                possible_doors =[1, 2]
                open_door = random.choice(possible_doors)
                if mode == "stay":
                    correct = correct+1
                else:
                    pass
            if correct_door == 1:
                open_door = 2
                if mode == "change":
                    correct = correct+1
                else:
                    pass
            if correct_door == 2:
                open_door = 1
                if mode == "change":
                    correct = correct+1

        print("original picked door:", picked_door)
        print("correct door:", correct_door)
        print("mode:", mode)
        print("opened door:", open_door)
        print("correct guesses:", correct)

    print("\n \n")
    print("statistics:")
    print("rounds:", rounds)
    print("correct guesses:",correct)
    print("mode:", mode)
    print("correct doors:")
    print("door 1 was correct:", times_door_1_was_correct)
    print("door 2 was correct:", times_door_2_was_correct)
    print("door 3 was correct:", times_door_3_was_correct)
def MHsimulation():
    configure_simulation();



if __name__ == '__main__':
    MHsimulation();


