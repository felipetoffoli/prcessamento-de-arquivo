from pypdf import PdfReader
from PIL import Image
import io
from bitstring import BitArray
from pdf2image import  convert_from_bytes

pdf_file = 'HelloWorld.pdf'
pdf_reader = PdfReader(pdf_file)

bitstream = ''
pdf_content = ''
bytes_io = io.BytesIO(b'\x48\x65\x6C\x6C\x6F')
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    page_text = page.extract_text()
    pdf_content += page_text
    
binary_data = bytes_io.getvalue()
bitstream = BitArray(bytes=binary_data)
with open('HelloWorld.text.txt', 'w') as file:
    file.write(pdf_content)
with open('HelloWorld.bitstram.txt', 'w') as file:
    file.write(bitstream.bin)
print("Imagem salva como 'HelloWorld.txt'")


with io.open('HelloWorld.bitstram.txt', 'r') as file:
    bitstream = BitArray(bin=file.read())

# Converter a sequência binária em bytes
image_data = bitstream.tobytes()

images = convert_from_bytes(image_data, fmt="jpeg")



print("Imagem salva como 'HelloWorld.jpg'")