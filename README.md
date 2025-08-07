# TASK MANAGER BOT
Test untuk tutor Python LVL 3

## Pre-requisite
Terlampir dalam `requirements.txt`. Lakukan instalasi dengan command berikut:

> `pip install -r requirements.txt`

## Test
Untuk melakukan test pada beberapa perintah yang dibuat dalam command.py harap ikut langkah berikut:
> 1. Buka terminal
> 2. ketik `python -m unittest discover tests`
> 3. Hasil akan menunjukkan 'OK' pada terminal
> 4. **WAJIB!** Jalankan `python runaftertest.py`

## Startup
Untuk mencoba program pastikan
> 1. Anda telah menginstall aplikasi discord
> 2. Anda telah memiliki token bot (cara mendapatkannya cari saja di youtube)
> 3. Setelah mendapatkan token bot, buka `bot.py` lalu simpan token di dalam variable `TOKEN`
> 4. buat database dengan command `python database.py`
> 5. jalankan program dengan command `python bot.py`

## How To
> 1. Menambah tugas `!add_task <tugasnya (str)>
> 2. Menandai tugas `!complete_task <id tugas (int)>
> 3. Menghapus tugas `!delete_task <id tugas (int)>
> 4. Melihat semua tugas `!show_task`

Feedback silahkan sampaikan saja
