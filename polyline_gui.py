import tkinter as tk
from tkinter import ttk, messagebox

from polyline_converter import parse_vector, convert_vectors


def parse_vectors_string(vectors_str: str):
    tokens = [tok for tok in vectors_str.split(')') if tok.strip()]
    return [parse_vector(tok + ')') for tok in tokens]


def on_convert():
    try:
        vectors = parse_vectors_string(vectors_entry.get())
        params = (int(p1_entry.get()), int(p2_entry.get()), int(p3_entry.get()))
        thresholds = (
            int(t1_entry.get()),
            int(t2_entry.get()),
            int(t3_entry.get()),
        )
        names = (n1_entry.get() or 'Param1', n2_entry.get() or 'Param2', n3_entry.get() or 'Param3')
        result = convert_vectors(vectors, params, thresholds, names)
        output_var.set(result)
    except Exception as exc:
        messagebox.showerror("Error", str(exc))


root = tk.Tk()
root.title("Polyline Converter")

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0, sticky="nsew")

# vectors input
vectors_label = ttk.Label(main_frame, text="Vectors")
vectors_label.grid(row=0, column=0, sticky="w")
vectors_entry = ttk.Entry(main_frame, width=40)
vectors_entry.grid(row=0, column=1, columnspan=5, sticky="ew")

# params
params_label = ttk.Label(main_frame, text="Params")
params_label.grid(row=1, column=0, sticky="w")
p1_entry = ttk.Entry(main_frame, width=5)
p1_entry.grid(row=1, column=1)
p2_entry = ttk.Entry(main_frame, width=5)
p2_entry.grid(row=1, column=2)
p3_entry = ttk.Entry(main_frame, width=5)
p3_entry.grid(row=1, column=3)

# thresholds
thresh_label = ttk.Label(main_frame, text="Thresholds")
thresh_label.grid(row=2, column=0, sticky="w")
t1_entry = ttk.Entry(main_frame, width=5)
t1_entry.grid(row=2, column=1)
t2_entry = ttk.Entry(main_frame, width=5)
t2_entry.grid(row=2, column=2)
t3_entry = ttk.Entry(main_frame, width=5)
t3_entry.grid(row=2, column=3)

# names
names_label = ttk.Label(main_frame, text="Names")
names_label.grid(row=3, column=0, sticky="w")
n1_entry = ttk.Entry(main_frame, width=8)
n1_entry.grid(row=3, column=1)
n2_entry = ttk.Entry(main_frame, width=8)
n2_entry.grid(row=3, column=2)
n3_entry = ttk.Entry(main_frame, width=8)
n3_entry.grid(row=3, column=3)

convert_button = ttk.Button(main_frame, text="Convert", command=on_convert)
convert_button.grid(row=4, column=0, columnspan=4, pady=5)

output_var = tk.StringVar()
output_label = ttk.Label(main_frame, textvariable=output_var)
output_label.grid(row=5, column=0, columnspan=4)

root.mainloop()
