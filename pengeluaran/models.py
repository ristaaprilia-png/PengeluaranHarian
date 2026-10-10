"""Class dan fungsi untuk mengelola data pengeluaran."""


class Pengeluaran:
    """Mewakili satu catatan pengeluaran harian."""

    def __init__(self, **kwargs):
        # Mengambil data berdasarkan nama atribut yang diberikan.
        self.tanggal = str(kwargs.get("tanggal", "")).strip()
        self.kategori = str(kwargs.get("kategori", "")).strip()
        self.keterangan = str(kwargs.get("keterangan", "")).strip()
        self.nominal = int(kwargs.get("nominal", 0))

    def ke_baris(self):
        """Mengubah data pengeluaran menjadi satu baris teks."""
        return (
            f"{self.tanggal};{self.kategori};"
            f"{self.keterangan};{self.nominal}\n"
        )

    def ke_dict(self):
        """Mengubah data pengeluaran menjadi dictionary."""
        return {
            "tanggal": self.tanggal,
            "kategori": self.kategori,
            "keterangan": self.keterangan,
            "nominal": self.nominal,
        }

    @classmethod
    def dari_baris(cls, baris):
        """Membaca satu baris teks dan mengubahnya menjadi objek."""
        bagian = baris.strip().split(";")

        if len(bagian) != 4:
            raise ValueError("Format data pengeluaran tidak valid.")

        tanggal, kategori, keterangan, nominal = bagian

        return cls(
            tanggal=tanggal,
            kategori=kategori,
            keterangan=keterangan,
            nominal=int(nominal),
        )


class PengelolaPengeluaran:
    """Mengelola kumpulan data pengeluaran."""

    def __init__(self, *data):
        # *data memungkinkan beberapa objek dimasukkan sekaligus.
        self.data = list(data)

    def tambah(self, pengeluaran):
        """Menambahkan data pengeluaran ke dalam daftar."""
        self.data.append(pengeluaran)

    def semua(self):
        """Mengembalikan daftar seluruh pengeluaran."""
        return list(self.data)


def buat_pengeluaran(**kwargs):
    """Membuat objek Pengeluaran dari data yang diberikan."""
    return Pengeluaran(**kwargs)


if __name__ == "__main__":
    # Menguji pembuatan objek saat file dijalankan secara langsung.
    contoh = buat_pengeluaran(
        tanggal="10-10-2026",
        kategori="Makan",
        keterangan="Makan siang",
        nominal=20000,
    )

    print(contoh.ke_dict())
