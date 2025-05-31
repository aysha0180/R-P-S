import streamlit as st

st.title("🔐 Caesar Cipher")
st.subheader("Encode or Decode Your Secret Messages 👀")

alphabet = [chr(i) for i in range(97, 123)]  # ['a' to 'z']

def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            new_position = (alphabet.index(letter) + shift_amount) % 26
            output_text += alphabet[new_position]
    return output_text.title()

# 🧭 User Inputs
direction = st.radio("Select action:", ["Encode", "Decode"])
text = st.text_input("Type your message:")
shift = st.number_input("Shift number:", min_value=1, max_value=25, step=1)

if st.button("Go!"):
    if not text:
        st.warning("Enter a message to proceed!")
    else:
        result = caesar(encode_or_decode=direction.lower(), original_text=text.lower(), shift_amount=int(shift))
        st.success(f"Here's the {direction.lower()}d result:")
        st.code(result, language='text')

