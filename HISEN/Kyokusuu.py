kyokusuu = ["一","二","三","四","五","六","七","八","九","十","十一","十二"]


def kyoku(nenshi,gessho):
    if nenshi - gessho >= 0:
        index = nenshi - gessho
        return kyokusuu[index]
    else:
        index = nenshi - gessho + 12
        return kyokusuu[index]

def tyuya(gessho):
    if gessho < 2 or gessho > 7:
        return "昼"
    else:
        return "夜"
