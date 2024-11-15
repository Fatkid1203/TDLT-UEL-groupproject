def filter_numbers(N):
    """Phân loại các số từ 1 đến N thành số nguyên tố, số chẵn và số lẻ."""
    primes = []
    evens = []
    odds = []

    for i in range(1, N + 1):
        # Kiểm tra số nguyên tố
        if i <= 1:
            continue  # Bỏ qua các số nhỏ hơn hoặc bằng 1
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

        # Kiểm tra số chẵn và số lẻ
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return primes, evens, odds  # Trả về ba danh sách