#!/mnt/c/Users/Honza/Projects/PDFconvertor/env/bin/python

from pdf2image import convert_from_path
import img2pdf
import os
import sys
 

# Store PDF with convert_from_path function


def makeCleanPDF(pathToPDF):
    images = convert_from_path(pathToPDF)
    
    for i in range(len(images)):
    
        # Save pages as images in the pdf
        page_name = 'page'+ str(i) +'.jpg'
        images[i].save(page_name, 'JPEG')
        print(f"Image {page_name} created.")

    # images to PDF
    dirname = "."
    imgs = []
    for fname in os.listdir(dirname):
        if not fname.endswith(".jpg"):
            continue
        path = os.path.join(dirname, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)
    with open(f"{pathToPDF[:-3]}_v2.pdf","wb") as f:
        f.write(img2pdf.convert(imgs))
        print(f"{pathToPDF[:-3]}_v2.pdf.")


    # delete images

    files_in_directory = os.listdir(dirname)
    filtered_files = [file for file in files_in_directory if file.endswith(".jpg")]
    for file in filtered_files:
        path_to_file = os.path.join(dirname, file)
        os.remove(path_to_file)
        print(f"Image {file} deleted!")


#pdf_name = input("Insert path: ")
#makeCleanPDF(pdf_name)