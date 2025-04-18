import streamlit as st
import time

class ShelfSimulator:
    def __init__(self):
        self.bottles = 10
        self.price = 10.0
        self.is_discounted = False

    def purchase(self):
        if self.bottles > 0:
            self.bottles -= 1
            if self.bottles <= 5:
                st.warning("Refill Alert: Add 5 bottles to shelf!")
                self.bottles += 5

    def apply_discount(self):
        if not self.is_discounted:
            self.price = self.price * 0.9
            self.is_discounted = True
            return f"New Price: ${self.price:.2f}"
        return "Discount already applied"

def main():
    st.title("Smart Shelf Simulator")
    
    if 'shelf' not in st.session_state:
        st.session_state.shelf = ShelfSimulator()

    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Purchase"):
            st.session_state.shelf.purchase()
            
    with col2:
        if st.button("Apply Discount"):
            message = st.session_state.shelf.apply_discount()
            st.write(message)

    st.write(f"Bottles on shelf: {st.session_state.shelf.bottles}")
    st.write(f"Current Price: ${st.session_state.shelf.price:.2f}")

if __name__ == "__main__":
    main()
