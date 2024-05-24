import random
import tkinter as tk

def calculate_parity_bits(data):
    m = len(data)
    r = 0
    while 2**r < m + r + 1:
        r += 1
    
    hamming_code = [0] * (m + r)
    j = 0
    for i in range(1, m + r + 1):
        if i & (i - 1) != 0:
            hamming_code[i - 1] = int(data[j])
            j += 1

    for i in range(r):
        parity_bit_index = 2**i - 1
        parity_bit_value = 0
        for j in range(1, m + r + 1):
            if j & (1 << i):
                parity_bit_value ^= hamming_code[j - 1]
        hamming_code[parity_bit_index] = parity_bit_value

    return hamming_code

def flip_bit(data):
    index = random.randint(0, len(data) - 1)
    data[index] = '1' if data[index] == '0' else '0'
    return data

def calculate_syndrome(received_code):
    m = len(received_code)
    r = 0
    while 2**r < m:
        r += 1
    syndrome = [0] * r
    for i in range(r):
        parity_bit_index = 2**i - 1
        parity_bit_value = 0
        for j in range(1, m + 1):
            if j & (1 << i):
                parity_bit_value ^= int(received_code[j - 1])
        syndrome[i] = parity_bit_value
    return syndrome

def detect_error_position(syndrome):
    error_position = 0
    for i, bit in enumerate(syndrome):
        error_position += bit * 2**i
    return error_position

def simulate():
    selected_option = bit_options.get()
    if selected_option not in ['4', '8', '16']:
        label_info.config(text="Bit sayısı 4, 8 veya 16 olmalı!")
        return
    
    label_info.config(text="")
    
    bit_count = int(selected_option)
    clear_bit_entry_widgets()
    create_bit_entry_widgets(bit_count)

def create_bit_entry_widgets(bit_count):
    for i in range(bit_count):
        label_bit = tk.Label(window, text="Bit {}: ".format(i+1))
        label_bit.grid(row=i+7, column=0)
        label_bits.append(label_bit)
        
        entry_bit = tk.Entry(window)
        entry_bit.grid(row=i+7, column=1)
        entry_bits.append(entry_bit)
    
    button_calculate.grid(row=bit_count+7, columnspan=2)

def clear_bit_entry_widgets():
    for label in label_bits:
        label.destroy()
    label_bits.clear()
    for entry in entry_bits:
        entry.destroy()
    entry_bits.clear()

def calculate_and_display():
    data = []
    for entry in entry_bits:
        bit = entry.get()
        if bit not in ['0', '1']:
            label_info.config(text="Her bit 0 veya 1 olmalı!")
            return
        data.append(bit)
    
    label_info.config(text="")
    
    label_girilen_data_code.config(text="Girilen Data: " + ''.join(map(str,data)))
    
    hamming_code = calculate_parity_bits(data)
    label_hamming_code.config(text="Girilen Datanın Hamming Kod'u: " + ''.join(map(str, hamming_code)))
    
    received_code = flip_bit(list(hamming_code))
    label_received_code.config(text="Alınan Hata: " + ''.join(map(str, received_code)))
    
    syndrome = calculate_syndrome(received_code)
    label_syndrome.config(text="Syndrome: " + ''.join(map(str, syndrome)))
    
    error_position = detect_error_position(syndrome)
    label_error_position.config(text="Error Pozisyonu: " + str(error_position))

# Create Tkinter window
window = tk.Tk()
window.title("Hamming Error-Correcting Simülatörü")
window.geometry("400x850")
text_var = tk.StringVar()
text_var.set("HOŞ GELDİNİZ")

# Create the label widget with all options





# Create and place widgets
title_label=tk.Label(window, 
                 textvariable=text_var,       
                 bg="orange",      
                 height=4,              
                 width=60,              
                 bd=3,                  
                 font=("Times", 9, "bold "), 
                 cursor="hand2",   
                 fg="black",            
                 justify=tk.CENTER,    
                 relief=tk.RAISED,        
                )
title_label.grid(row=0, columnspan=20)

label_bit_count = tk.Label( window,
                            height=2,              
                            width=60,  
                            text="BİT SAYISI",
                            bg="lightgrey",bd=3,
                            fg="red",
                            font=("Arial", 9, "bold underline"),
                            relief=tk.RAISED,
                            justify=tk.CENTER,
                            )

label_bit_count.grid(row=1, column=0, columnspan=3)
bit_options = tk.StringVar(window)
bit_options.set("4")  # Default bit count option
bit_count_menu = tk.OptionMenu(window, bit_options, "4", "8", "16")
bit_count_menu.grid(row=3)

button_start = tk.Button(window, text="OK", command=simulate)
button_start.grid(row=3,column=1)

label_bosluk = tk.Label(window,
                            height=2,              
                            width=60,  
                            bg="lightgrey",bd=3,
                            fg="red",
                            font=("Arial", 9, "bold underline"),
                            relief=tk.RAISED, 
                            text="BİT GİRİŞİ")
label_bosluk.grid(row=4, columnspan=2)



label_info = tk.Label(window, text="")
label_info.grid(row=25, columnspan=3)

label_bits = []
entry_bits = []

button_calculate = tk.Button(window, text="Hesapla/Tekrar Hesapla", command=calculate_and_display)

label_sonuc = tk.Label(window,
                            height=2,              
                            width=60,  
                            bg="lightgrey",bd=3,
                            fg="red",
                            font=("Arial", 9, "bold underline"),
                            relief=tk.RAISED, 
                            text="SONUÇLAR ")
label_sonuc.grid(row=29, columnspan=2)

label_girilen_data_code = tk.Label(window,
                            height=2,              
                            width=60,  
                            bg="lightgrey",bd=3,
                            fg="black",
                            font=("Arial", 9, "bold"),
                            relief=tk.RAISED, 
                            text="")
label_girilen_data_code.grid(row=30, columnspan=2)

label_hamming_code = tk.Label(window,height=2,              
                            width=60,  
                            bg="lightgrey",bd=3,
                            fg="black",
                            font=("Arial", 9, "bold"),
                            relief=tk.RAISED, 
                            text="")
label_hamming_code.grid(row=31, columnspan=2)

label_received_code = tk.Label(window, height=2,              
                            width=60,  
                            bg="lightgrey",bd=3,
                            fg="black",
                            font=("Arial", 9, "bold"),
                            relief=tk.RAISED, 
                            text="")
label_received_code.grid(row=32, columnspan=2)

label_syndrome = tk.Label(window, height=2,              
                            width=60,  
                            bg="lightgrey",bd=3,
                            fg="black",
                            font=("Arial", 9, "bold"),
                            relief=tk.RAISED, 
                            text="")
label_syndrome.grid(row=33, columnspan=2)

label_error_position = tk.Label(window, height=2,              
                            width=60,  
                            bg="lightgrey",bd=3,
                            fg="black",
                            font=("Arial", 9, "bold"),
                            relief=tk.RAISED, 
                            text="")
label_error_position.grid(row=34, columnspan=2)

#Tkinter event loop başlangıcı buradadır
window.mainloop()
