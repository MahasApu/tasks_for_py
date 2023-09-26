benchmarks = ["best case", "worst case", "medium rare case"]
algos = ["quick sort00000000", "merge sort", "bubble sort"]
results = [[1.23, 1.56, 2.0],
           [3.3, 2.9, 3888.9],
           [11.11, 32377777777776776.555, 22.7]]


def format_table(benchmarks, algos, results):

    # максимальная длина для колонки с Benchmarks
    y = max(map(len, benchmarks))
    mx_bench = max(y, len("Benchmarks"))

    # заполнение списка шириной для столбцов
    # путем нахождения максимальной длины элемента
    cur_algos = [-1 for i in algos]

    for i, bench in enumerate(benchmarks):
        for j in range(len(algos)):
            cur_algos[j] = max(cur_algos[j], len(str(results[i][j])))

    # Конечный список ширины столбцов, для которого сравниваются
    # длины элементов и заголовки столбцов
    mxlen = [-1 for i in algos]

    for i in range(len(cur_algos)):
        mxlen[i] = max(cur_algos[i], len(algos[i]))

    print("|", "{header:<{header_indent}}".format(header="Benchmark",
                                            header_indent=mx_bench),
          "|", " | ".join("{:<{len}}".format(elem, len=mxlen[i])
           for i, elem in enumerate(algos)), "|")

    # длина разделителя --- равна сумме максимальных длин слов + самое длинное
    # слово среди benchmarks + количество " | ", равное трем.
    print("|", '-' * (sum(mxlen) + mx_bench + 3*len(algos)), "|")

    for i, bench in enumerate(benchmarks):

        print("|", "{:<{len}}".format(bench, len=mx_bench), "|",
              " | ".join("{:<{len}}".format(elem, len=mxlen[j])
              # вывод элемента из results[i] + длина из mxlen
              # по индексу элемента из results[i]
              for j, elem in enumerate(results[i])), "|")


format_table(benchmarks, algos, results)
print("\n")
