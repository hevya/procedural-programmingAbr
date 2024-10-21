# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines_in_book = 50
symbols_in_line = 25
symbol_byte = 4
disk_mb = 1.44

one_book_bytes = pages * lines_in_book * symbols_in_line * symbol_byte
disk_byte = disk_mb * 1024**2
books_in_disk = disk_byte // one_book_bytes
print("Количество книг, помещающихся на дискету:", int(books_in_disk))
