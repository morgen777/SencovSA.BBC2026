
import random

MAZE = [
    "#########",
    "#S..#...#",
    "#.#...M.#",
    "#.#.##..#",
    "#...C...#",
    "###.##..#",
    "#.......#",
    "#.#####P#",
    "#########"
]

DIRECTIONS = {
    "w": (-1, 0, "вверх"),
    "s": (1, 0, "вниз"),
    "a": (0, -1, "влево"),
    "d": (0, 1, "вправо")
}


def reveal(player, seen):
    y, x = player

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            ny = y + dy
            nx = x + dx

            if 0 <= ny < len(MAZE) and 0 <= nx < len(MAZE[0]):
                seen.add((ny, nx))


def show_maze(maze, player, seen):
    print("\nЛабиринт:")

    for y in range(len(maze)):
        line = []

        for x in range(len(maze[y])):
            if (y, x) == player:
                line.append("@")

            elif (y, x) not in seen:
                line.append("?")

            elif maze[y][x] == ".":
                line.append(" ")

            else:
                line.append(maze[y][x])

        print(" ".join(line))


def fight(hp, monster_hp, damage):
    print("\nНа тебя напал гоблин!")

    while monster_hp > 0 and hp > 0:
        print(f"\nТвоё HP: {hp} | HP гоблина: {monster_hp}")
        choice = input("1 - Атаковать, 2 - Убежать: ").strip()

        if choice == "1":
            dmg = random.randint(*damage)
            monster_hp -= dmg
            print(f"Ты наносишь гоблину {dmg} урона.")

            if monster_hp > 0:
                enemy_dmg = random.randint(3, 8)
                hp -= enemy_dmg
                print(f"Гоблин наносит тебе {enemy_dmg} урона.")

        elif choice == "2":
            print("Ты убежал от гоблина!")
            return hp, False

        else:
            print("Нужно выбрать 1 или 2.")

    if hp <= 0:
        print("\nТы проиграл!")
        return hp, False

    print("\nТы победил гоблина!")
    return hp, True


def main():
    maze = [list(row) for row in MAZE]

    hp = 100
    damage = (10, 20)

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "S":
                player = (y, x)
                maze[y][x] = "."

    seen = set()
    reveal(player, seen)

    print("Добро пожаловать в игру «Лабиринт»!")
    print("Твоя задача — найти портал и выбраться.")
    print("Управление: W - вверх, S - вниз, A - влево, D - вправо.")
    print("\nИсследуй лабиринт, чтобы открывать новые клетки!")

    while hp > 0:
        show_maze(maze, player, seen)

        print(f"\nТвоё здоровье: {hp}")
        print("Доступные направления:")

        available = []

        for key, (dy, dx, name) in DIRECTIONS.items():
            ny = player[0] + dy
            nx = player[1] + dx

            if maze[ny][nx] != "#":
                available.append(key)
                print(f"{key.upper()} - {name}")

        choice = input("\nКуда пойдём? ").lower().strip()

        if choice not in available:
            print("Туда пройти нельзя!")
            continue

        dy, dx, name = DIRECTIONS[choice]

        ny = player[0] + dy
        nx = player[1] + dx

        cell = maze[ny][nx]

        if cell == "M":
            hp, won = fight(hp, 30, damage)

            if hp <= 0:
                break

            if won:
                maze[ny][nx] = "."
                player = (ny, nx)

        elif cell == "C":
            print("\nТы нашёл сундук!")
            print("Внутри лежит меч.")
            print("Твой урон увеличился!")

            damage = (20, 35)
            maze[ny][nx] = "."
            player = (ny, nx)

        elif cell == "P":
            print("\nТы нашёл портал!")
            print("Поздравляем! Ты выбрался из лабиринта!")
            break

        else:
            player = (ny, nx)

        reveal(player, seen)

    if hp <= 0:
        print("\nИгра окончена. Попробуй ещё раз!")


if __name__ == "__main__":
    main()
