"""Fungsi untuk mengolah data pengeluaran."""


def hitung_total(data):
    """Menghitung total seluruh nominal pengeluaran."""
    return sum(item.nominal for item in data)


def hitung_rata_rata(data):
    """Menghitung rata-rata nominal pengeluaran."""
    if not data:
        return 0

    return hitung_total(data) / len(data)


def urutkan_pengeluaran(data, urutan="terbesar"):
    """Mengurutkan pengeluaran berdasarkan nominal."""
    if urutan == "terbesar":
        return sorted(data, key=lambda item: item.nominal, reverse=True)

    return sorted(data, key=lambda item: item.nominal)


def kelompokkan_kategori(data):
    """Menghitung jumlah pengeluaran untuk setiap kategori."""
    hasil = {}

    for item in data:
        kategori = item.kategori
        hasil[kategori] = hasil.get(kategori, 0) + item.nominal

    return hasil


def pengeluaran_terbesar(data):
    """Mencari pengeluaran dengan nominal paling besar."""
    if not data:
        return None

    return max(data, key=lambda item: item.nominal)
