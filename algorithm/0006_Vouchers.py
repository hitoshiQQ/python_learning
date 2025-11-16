def max_profit(vouchers):
    # vouchers: список кортежей (d, c)
    # d — сколько дней осталось у путёвки (целое, <= 30)
    # c — цена одного дня (целое, <= 100)
    # Возвращает максимальную суммарную прибыль (целое).

    n = len(vouchers)
    if n == 0:
        return 0

    msize = 1 << n
    # dp[mask] = максимальная прибыль при том, что проданы путёвки,
    # соответствующие битам mask
    # и свободны дни с t = popcount(mask)+1 и далее.
    # Инициализируем очень маленьким числом (или -inf), кроме dp[0] = 0
    dp = [-10**18] * msize
    dp[0] = 0

    # Проходим по всем маскам
    for mask in range(msize):
        # сколько путёвок уже продано => следующий день t
        sold = mask.bit_count()   # Python 3.8+: fast popcount
        t = sold + 1

        # Для каждой незаданной (непроданной) путёвки
        # j — попробуем продать её в день t
        for j in range(n):
            if (mask >> j) & 1:
                continue  # путёвка j уже продана в этом маске

            d, c = vouchers[j]
            days_left = d - (t - 1)      # при продаже в день t
            gain = c * days_left if days_left > 0 else 0

            nmask = mask | (1 << j)
            val = dp[mask] + gain
            # обновляем dp для нового состояния
            if val > dp[nmask]:
                dp[nmask] = val

    # Мы можем не продавать все путёвки,
    # поэтому ответ — максимум по всем состояниям
    return max(dp)


# -----------------------
# ввод / вывод
# -----------------------
n = int(input().strip())
vouchers = [tuple(map(int, input().split())) for _ in range(n)]
print(max_profit(vouchers))
