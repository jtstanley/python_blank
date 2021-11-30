import cProfile
import pstats
import blank_lib


# Here is main that runs methods from blank_lib
def main():
    blank_lib.func()


# Here is the function that profiles main
def profile_main():
    with cProfile.Profile() as prof:
        main()
        
        stats = pstats.Stats(prof)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()


if __name__ == '__main__':
    profile_main()
