import PyPDF2
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.ttk as ttk

def split_pdf(pdf_file, progress_bar):
    # Split the PDF into 2-page sections
    section_num = 1
    pdf = PyPDF2.PdfReader(open(pdf_file, "rb"))
    for i in range(0, len(pdf.pages), 2):
        section = PyPDF2.PdfWriter()
        section.add_page(pdf.pages[i])
        section.add_page(pdf.pages[i+1])

        # Save each section with an iterative naming convention
        section_filename = save_location_var.get() + "/" + str(section_num) + ".pdf"
        with open(section_filename, "wb") as f:
            section.write(f)
        section_num += 1
        progress_bar["value"] = (i+2) / len(pdf.pages) * 100
        root.update_idletasks()
        
        # Update the status bar
        status_var.set("Last saved PDF: " + section_filename)
        

# Create the GUI
root = tk.Tk()
root.title("MKUltra Production Engineering - PDF Splitter v1.0.0")

# Create a file browser
file_frame = tk.Frame(root)
file_frame.pack(pady=10)
file_label = tk.Label(file_frame, text="PDF File:")
file_label.pack(side="left")
file_var = tk.StringVar()
file_entry = tk.Entry(file_frame, textvariable=file_var, width=50)
file_entry.pack(side="left")
file_button = tk.Button(file_frame, text="Browse", command=lambda: file_var.set(filedialog.askopenfilename()))
file_button.pack(side="left")

# Create a file save location browser
save_location_frame = tk.Frame(root)
save_location_frame.pack(pady=10)
save_location_label = tk.Label(save_location_frame, text="Save Location:")
save_location_label.pack(side="left")
save_location_var = tk.StringVar()
save_location_entry = tk.Entry(save_location_frame, textvariable=save_location_var, width=50)
save_location_entry.pack(side="left")
save_location_button = tk.Button(save_location_frame, text="Browse", command=lambda: save_location_var.set(filedialog.askdirectory()))
save_location_button.pack(side="left")


# Create a progress bar
progress_frame = tk.Frame(root)
progress_frame.pack(pady=10)
progress_bar = ttk.Progressbar(progress_frame, length=500, mode="determinate")
progress_bar.pack()

# Create a status bar
status_var = tk.StringVar()
status_var.set("Last saved PDF: None")
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief="sunken", anchor="w")
status_bar.pack(side="bottom", fill="x")

# Create a split button
split_button = tk.Button(root, text="Split PDF", command=lambda: split_pdf(file_var.get(), progress_bar))
split_button.pack(pady=10)

root.mainloop()
