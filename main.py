from CaveGen import Cave
import Draw

if __name__ == '__main__':
    # Ask the user for cave size and wall density
    N = int(input("Enter the size of the cave (max 200): "))
    Temp = int(input("Enter the density of walls (1 ... 100): "))
    print("Generating...")

    # Create a cave object and simulate cave generation
    C = Cave(N,Temp)
    C.simulate()

    # Convert the cave to colors and draw it
    D = Draw.Draw(C.ReturnCols(),N)
    D.Show()