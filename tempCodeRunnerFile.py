
    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(10):
    # donwloadFile(url, i)

        p = multiprocessing.Process(target=donwloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
     p.join()