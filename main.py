from gol_engine import GOLEngine 

def main() -> None:
    gol = GOLEngine(100, 100)
    print(f"Game of life size :  {gol.width} x {gol.height} y")



    # gol.width = 120
    # print(f"Game of life size :  {gol.width} x {gol.height} y")
    # gol.height = 100
    # print(f"Game of life size :  {gol.width} x {gol.height} y")

    # gol.set_cell(3, 5, "alive")
    # print(f"Cell Value (3, 5) = {gol.get_cell(3, 5)}")

    # gol.randomize(0.75) # chaque cellule a 75% de chance d'etre vivant

    # gol.tick()
    
    # print(gol.to_string())

    if __name__ == "__main__":
        main()