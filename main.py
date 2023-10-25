from pypdf import PdfWriter , PdfReader 
from PIL import Image
import io
from bitstring import BitArray
from pdf2image import  convert_from_bytes
from uuid import uuid4
import img2pdf
import os

# capiturando arquivo
pdf_file = 'HelloWorld.pdf'
with io.open(pdf_file, 'rb') as file:
    varbinary = file.read()

# transformando em binary 01
bitarray = BitArray(bytes=varbinary)
bitstream = bitarray.bin
print(f'BITSTREAM: {bitstream[0:60]}...', )

pdf_reader = PdfReader(pdf_file)
pdf_content= ''
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    page_text = page.extract_text()
    pdf_content += page_text
    
print('TEXTO PDF: ', pdf_content)
# transformando binary 01 para arquvo novamente
new_bitarray = BitArray(bin=bitstream)

# salvando arquivo novamente
# with io.open('HelloWorld2.pdf', 'wb') as file:
#     file.write(new_bitarray.bytes)

images_from_bytes = convert_from_bytes(
                new_bitarray.bytes,
               # fmt="jpg",
                jpegopt={"quality": 100, "progressive": True, "optimize": True},
            )

name_files = str(uuid4())
for i, image in enumerate(images_from_bytes):
    image.save(f'images/{name_files}_{i + 1}.png', 'PNG')

diretorio_atual = os.getcwd()
pasta_images = os.path.join(diretorio_atual, 'images')
all_itens_folder = os.listdir(pasta_images)
itens_foler = []

for item in all_itens_folder:
    if item.startswith(name_files):
        itens_foler.append(os.path.join(pasta_images, item))
print(f'IMAGENS GERADAS: {itens_foler}')
new_pdf_name = f"{name_files}.pdf"
with open(new_pdf_name,"wb") as f:
	f.write(img2pdf.convert(itens_foler))
print(f"PDF CRIADO A PARTIR DAS IMAGENS: {new_pdf_name}")