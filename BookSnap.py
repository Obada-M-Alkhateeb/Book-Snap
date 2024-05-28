import fitz  # PyMuPDF
from pptx import Presentation
from pptx.util import Inches
from flask import Flask, request, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_presentation_with_text_and_images(text, images):
    presentation = Presentation()
    slide_text = presentation.slides.add_slide(presentation.slide_layouts[5])
    text_box_text = slide_text.shapes.add_textbox(left=0, top=0, width=presentation.slide_width, height=presentation.slide_height)
    text_frame_text = text_box_text.text_frame
    text_frame_text.text = text

    for image in images:
        slide_image = presentation.slides.add_slide(presentation.slide_layouts[5])
        left = top = Inches(1)
        image_width = presentation.slide_width - left * 2
        image_height = presentation.slide_height - top * 2
        slide_image.shapes.add_picture(image, left, top, width=image_width, height=image_height)

    return presentation

def extract_pdf_text_and_images(pdf_file_path):
    doc = fitz.open(pdf_file_path)
    full_text = ""
    images = []

    for page in doc:
        full_text += page.get_text()
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_path = os.path.join(UPLOAD_FOLDER, f"image{img_index}.png")
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
            images.append(image_path)

    doc.close()
    return full_text, images

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        extracted_text, extracted_images = extract_pdf_text_and_images(file_path)
        presentation = create_presentation_with_text_and_images(extracted_text, extracted_images)
        pptx_path = os.path.join(app.config['UPLOAD_FOLDER'], 'presentation.pptx')
        presentation.save(pptx_path)
        return send_file(pptx_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""import fitz  # PyMuPDF 
from pptx import Presentation 
from pptx.util import Inches 
from flask import Flask, request, send_file 
import os 
import nltk 
from nltk.tokenize import sent_tokenize 
 
app = Flask(__name__) 
UPLOAD_FOLDER = 'uploads' 
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
 
# Download NLTK resources (run only once) 
nltk.download('punkt') 
 
def create_presentation(chapter_texts, images): 
    presentation = Presentation() 
 
    for chapter_text in chapter_texts: 
        slide_layout = presentation.slide_layouts[5]  # Choose a slide layout 
        slide = presentation.slides.add_slide(slide_layout) 
        text_frame = slide.shapes.add_textbox(left=Inches(1), top=Inches(1), width=Inches(8), height=Inches(6)).text_frame 
        text_frame = text_box.text_frame
        text_frame.text = chapter_text 
 
    for image in images: 
        slide_layout = presentation.slide_layouts[5]  # Choose a slide layout 
        slide = presentation.slides.add_slide(slide_layout) 
        left = top = Inches(1) 
        image_width = Inches(8) 
        image_height = Inches(6) 
        slide.shapes.add_picture(image, left, top, width=image_width, height=image_height) 
 
    return presentation 
 
def extract_pdf_text_and_images(pdf_file_path): 
    doc = fitz.open(pdf_file_path) 
    chapter_texts = [] 
    images = [] 
 
    for page in doc: 
        text = page.get_text() 
        sentences = sent_tokenize(text) 
        words_count = 0 
        current_text = "" 
        for sentence in sentences: 
            words = sentence.split() 
            if words_count + len(words) <= 50: 
                current_text += sentence + " " 
                words_count += len(words) 
            else: 
                chapter_texts.append(current_text.strip()) 
                current_text = sentence + " " 
                words_count = len(words) 
        if current_text: 
            chapter_texts.append(current_text.strip()) 
 
        for img_index, img in enumerate(page.get_images(full=True)): 
            xref = img[0] 
            base_image = doc.extract_image(xref) 
            image_bytes = base_image["image"] 
            image_path = os.path.join(UPLOAD_FOLDER, f"image{img_index}.png") 
            with open(image_path, "wb") as image_file: 
                image_file.write(image_bytes) 
            images.append(image_path) 
 
    doc.close() 
    return chapter_texts, images 
 
@app.route('/upload', methods=['POST']) 
def upload_file(): 
    if 'file' not in request.files: 
        return 'No file part', 400 
    file = request.files['file'] 
    if file.filename == '': 
        return 'No selected file', 400 
    if file: 
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename) 
        file.save(file_path) 
        chapter_texts, extracted_images = extract_pdf_text_and_images(file_path) 
        presentation = create_presentation(chapter_texts, extracted_images) 
        pptx_path = os.path.join(app.config['UPLOAD_FOLDER'], 'presentation.pptx') 
        presentation.save(pptx_path) 
        return send_file(pptx_path, as_attachment=True) 
 
if __name__ == '__main__': 
    app.run(debug=True)"""




"""import fitz  # PyMuPDF 
from pptx import Presentation 
from pptx.util import Inches 
import os 
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize 
from tkinter import Tk, filedialog, messagebox, ttk 
import tkinter as tk

def summarize_text(text, max_words_per_slide): 
    sentences = sent_tokenize(text) 
    summary_sentences = [] 
    current_summary = "" 
    words_count = 0 
 
    for sentence in sentences: 
        words = word_tokenize(sentence) 
        if words_count + len(words) <= max_words_per_slide: 
            current_summary += sentence + " " 
            words_count += len(words) 
        else: 
            summary_sentences.append(current_summary.strip()) 
            current_summary = sentence + " " 
            words_count = len(words) 
     
    if current_summary: 
        summary_sentences.append(current_summary.strip()) 
 
    return summary_sentences 
 
def extract_pdf_content(pdf_file_path, max_images=5): 
    doc = fitz.open(pdf_file_path) 
    full_text = "" 
    images = [] 
    tables = [] 
 
    for page in doc: 
        full_text += page.get_text() 
        if len(images) < max_images: 
            for img_index, img in enumerate(page.get_images(full=True)): 
                if len(images) >= max_images: 
                    break 
                xref = img[0] 
                base_image = doc.extract_image(xref) 
                image_bytes = base_image["image"] 
                image_path = f"image{img_index}.png" 
                with open(image_path, "wb") as image_file: 
                    image_file.write(image_bytes) 
                images.append(image_path) 
 
        # Extract tables (for demonstration, we assume the table data is in text format) 
        for block in page.get_text("dict")["blocks"]: 
            if block["type"] == 0:  # Text block 
                table_text = "" 
                for line in block["lines"]: 
                    for span in line["spans"]: 
                        if span["text"].strip().startswith("|"):  # Simple table detection heuristic 
                            table_text += span["text"] + "\n" 
                if table_text: 
                    tables.append(table_text) 
 
    doc.close() 
    return full_text, images, tables 
 
def create_presentation(chapter_texts, images, tables): 
    presentation = Presentation() 
 
    for chapter_text in chapter_texts: 
        slide_layout = presentation.slide_layouts[5] 
        slide = presentation.slides.add_slide(slide_layout) 
        text_box = slide.shapes.add_textbox(left=Inches(1), top=Inches(1), width=Inches(8), height=Inches(6)) 
        text_frame = text_box.text_frame 
        text_frame.text = chapter_text 
 
    for image in images: 
        slide_layout = presentation.slide_layouts[5] 
        slide = presentation.slides.add_slide(slide_layout) 
        left = top = Inches(1) 
        image_width = Inches(8) 
        image_height = Inches(6) 
        slide.shapes.add_picture(image, left, top, width=image_width, height=image_height) 
 
    for table_text in tables: 
        slide_layout = presentation.slide_layouts[5] 
        slide = presentation.slides.add_slide(slide_layout) 
        text_box = slide.shapes.add_textbox(left=Inches(1), top=Inches(1), width=Inches(8), height=Inches(6)) 
        text_frame = text_box.text_frame 
        text_frame.text = table_text 
 
    return presentation 
 
def select_pdf(): 
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]) 
    if file_path: 
        try: 
            full_text, images, tables = extract_pdf_content(file_path, max_images=5) 
            summarized_texts = summarize_text(full_text, max_words_per_slide=50) 
            presentation = create_presentation(summarized_texts, images, tables) 
            pptx_path = os.path.splitext(file_path)[0] + "_summary.pptx" 
            presentation.save(pptx_path) 
            messagebox.showinfo("Success", f"Presentation saved as {pptx_path}") 
        except Exception as e: 
            messagebox.showerror("Error", str(e)) 
 
# Create a simple GUI 
root = Tk() 
root.title("Book Summary to PowerPoint") 
 
frame = ttk.Frame(root, padding="10") 
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S)) 
 
select_button = ttk.Button(frame, text="Select PDF", command=select_pdf) 
select_button.grid(row=0, column=0, pady=10) 
 
root.mainloop()"""

