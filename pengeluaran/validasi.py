"""Fungsi untuk memeriksa validitas data pengeluaran."""


class DataTidakValidError(Exception):
    """Error khusus ketika data pengeluaran tidak valid."""
    pass


def validasi_pengeluaran(pengeluaran):
    """Memeriksa kelengkapan dan kebenaran data pengeluaran."""

    if not pengeluaran.tanggal:
        raise DataTidakValidError("Tanggal tidak boleh kosong.")

    if not pengeluaran.kategori:
        raise DataTidakValidError("Kategori tidak boleh kosong.")

    if not pengeluaran.keterangan:
        raise DataTidakValidError("Keterangan tidak boleh kosong.")

    if pengeluaran.nominal <= 0:
        raise DataTidakValidError("Nominal harus lebih dari nol.")

    # Memastikan nominal yang disimpan berupa bilangan bulat.
    assert isinstance(pengeluaran.nominal, int)

    return True
