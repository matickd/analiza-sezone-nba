class igralec:
    def __init__(self, ime, ekipa, odigrane_igre, pike, asistence, skoki):
        self.ime = ime
        self.ekipa = ekipa
        self.odigrane_igre = odigrane_igre
        self.pike = pike
        self.asistence = asistence
        self.skoki = skoki

    def __str__(self):
        return f"{self.ime} ({self.ekipa}): {self.pike} PTS, {self.asistence} AST, {self.skoki} REB"

    def povprecje_tock(self):
        if self.odigrane_igre == 0:
            return 0
        return round(self.pike / self.odigrane_igre, 2)

    def povprecje_podaj(self):
        if self.odigrane_igre == 0:
            return 0
        return round(self.asistence / self.odigrane_igre, 2)

    def povprecje_skokov(self):
        if self.odigrane_igre == 0:
            return 0
        return round(self.skoki / self.odigrane_igre, 2)
