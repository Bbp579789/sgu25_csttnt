def main():
    try:
        with open("assignment.txt", "r") as file:
            n = int(file.readline())
            cost = [list(map(int, file.readline().split())) for _ in range(n)]
    except Exception as e:
        print("Lỗi khi đọc file:", e)
        return

    job_assigned = [False] * n
    total_cost = 0

    for i in range(n):
        min_cost = float('inf')
        job_index = -1
        for j in range(n):
            if not job_assigned[j] and cost[i][j] < min_cost:
                min_cost = cost[i][j]
                job_index = j
        if job_index != -1:
            job_assigned[job_index] = True
            total_cost += min_cost

    print("Tổng chi phí:", total_cost)

if __name__ == "__main__":
    main()
