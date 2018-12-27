# Coding challenge from codesignal called sledrun
# Gets different sled courses and determines which one to take(usually represented by the highest value).
# Sometimes you may want to take another route(usually represented by the second highest number if it is near the highest value)


def runs(elements, max_runs):
    run = []

    for i in elements:
        run += range(i+1)
        run = sorted(run)[::-1]
    print(sum(run[:max_runs]))


# Test run. Supposed to grab the highest number(8). With 5 max_runs. (8 + 7 + 6 + 5 + 4 = 30)
# runs([1, 8, 3], 5)


# Test run. Grabs highest number(20)
# However since the second highest number is near the highest number(19) then you may also grab that number.
# Keep in mind that max_runs is 4, so (20 + 19 + 19 + 18 = 76)
# runs([1, 19, 8, 20, 18], 4)
