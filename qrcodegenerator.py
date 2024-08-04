#STEPS
# 1.Install all the packages needed
# 2.Create a function that collects the  text and converts it to a qrcode
# 3.Save the qrcode as an image
# 4.run the function
#1
import qrcode #imports qrcode
#2
def generate_qrcode(text): #A function that takes in a text and converts it to a qrcode
#3    
    qr = qrcode.QRCode( #Creating a QRCode Object:
        version = 1, #Sets the size of the QR code
        error_correction = qrcode.constants.ERROR_CORRECT_L, #sets the error correction level of the code.
        box_size = 10,#Sets the size of each box in the QR code.
        border = 4,#Sets the border size of the QR code.
        )
#4        
    qr.add_data(text) #adds the text data to the QR code.
#5
    qr.make(fit=True)#Fit the QR Code to the Data
#6
    img = qr.make_image(fill_color="black", back_color="white")#creates an image of the QR code with black boxes and a white background.
#7
    img.save("qrcode007.png") #saves the generated QR code image        
#8
url = input("Enter your url:") #This line prompts the user to input URL
generate_qrcode(url)  #Generates the QR Code
    
#!!!!! ///THE QRCODE WILL BE SAVED ON THE FOLDER OF THIS FILE///     
#If not working try changing the file name(img.save("qrcode006.png")) 
#███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗
#████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝
#██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝ 
#██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝  
#██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║   
#╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝   
# █████╗ ██████╗ ██╗  ██╗██╗     ██╗██╗████████╗██╗  ██╗    ████████╗██████╗ 
#██╔══██╗██╔══██╗██║  ██║██║     ██║██║╚══██╔══╝██║  ██║    ╚══██╔══╝██╔══██╗
#███████║██████╔╝███████║██║     ██║██║   ██║   ███████║       ██║   ██████╔╝
#██╔══██║██╔══██╗██╔══██║██║██   ██║██║   ██║   ██╔══██║       ██║   ██╔═══╝ 
#██║  ██║██████╔╝██║  ██║██║╚█████╔╝██║   ██║   ██║  ██║       ██║   ██║     
#╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝ ╚════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝       ╚═╝   ╚═╝     
                                                                            
                                                                                                       
                                                                                                                                                                                                             
                                                                                                       
                                                                                                       
   
