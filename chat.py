import streamlit as st
from openai import OpenAI
import time


class DepressionSupportChatbot:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="<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>",
        )
        self.initialize_session_state()

    def initialize_session_state(self):
        if 'user_info' not in st.session_state:
            st.session_state.user_info = {
                "name": "",
                "age": "",
                "location": "",
                "primary_concerns": ""
            }
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []
        if 'user_info_collected' not in st.session_state:
            st.session_state.user_info_collected = False

    def get_user_info(self):
        st.title("Depression Support Chatbot")
        st.write("Welcome to the Depression Support Chatbot.")
        st.write("To help me provide better support, could you share a little about yourself?")

        with st.form("user_info_form"):
            name = st.text_input("What's your name? (optional)")
            age = st.text_input("How old are you? (optional)")
            location = st.text_input("Where are you from? (optional)")
            concerns = st.text_area(
                "What brings you here today? (You can share as much or as little as you're comfortable with)")

            submitted = st.form_submit_button("Start Chat")

            if submitted:
                st.session_state.user_info = {
                    "name": name if name else "Friend",
                    "age": age,
                    "location": location,
                    "primary_concerns": concerns if concerns else "Not specified"
                }

                # Add initial context to conversation history
                st.session_state.conversation_history = [{
                    "role": "system",
                    "content": f"You are a compassionate, knowledgeable depression support assistant. \
                                The user's name is {st.session_state.user_info['name']}. \
                                They are {st.session_state.user_info['age']} years old from {st.session_state.user_info['location']}. \
                                Their primary concerns are: {st.session_state.user_info['primary_concerns']}. \
                                Provide empathetic, non-judgmental support. Offer practical coping strategies \
                                and encourage professional help when appropriate. Validate their feelings \
                                while gently challenging negative thought patterns when needed."
                }]

                # Add welcome message
                st.session_state.conversation_history.append({
                    "role": "assistant",
                    "content": f"Hello {st.session_state.user_info['name']}, I'm here to listen and support you. You can talk to me about anything you're feeling. How are you doing today?"
                })

                st.session_state.user_info_collected = True
                st.rerun()

    def chat_interface(self):
        st.title(f"Mindful Companion - Chatting with {st.session_state.user_info['name']}")

        # Display conversation history (skip system message)
        for message in st.session_state.conversation_history[1:]:
            if message["role"] == "assistant":
                with st.chat_message("assistant"):
                    st.write(message["content"])
            elif message["role"] == "user":
                with st.chat_message("user"):
                    st.write(message["content"])

        # User input
        if user_input := st.chat_input("Type your message here..."):
            # Add user message to conversation
            with st.chat_message("user"):
                st.write(user_input)

            st.session_state.conversation_history.append({"role": "user", "content": user_input})

            # Check for crisis keywords
            if self.detect_crisis(user_input):
                self.handle_crisis_protocol()
            else:
                # Show typing indicator
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        # Generate response
                        response = self.generate_response()
                        st.write(response)

                st.session_state.conversation_history.append({"role": "assistant", "content": response})

    def generate_response(self):
        completion = self.client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "Depression Support Chatbot",
            },
            model="deepseek/deepseek-r1-0528",
            messages=st.session_state.conversation_history,
            temperature=0.7
        )
        return completion.choices[0].message.content

    def detect_crisis(self, text):
        crisis_keywords = ['suicide', 'kill myself', 'end it all', 'want to die', 'harm myself']
        return any(keyword in text.lower() for keyword in crisis_keywords)

    def handle_crisis_protocol(self):
        with st.chat_message("assistant"):
            st.warning("I'm concerned about what you're sharing. Your life is valuable and important.")
            st.write("Please consider reaching out to one of these resources immediately:")
            st.write("- National Suicide Prevention Lifeline: 1-800-273-TALK (8255)")
            st.write("- Crisis Text Line: Text HOME to 741741")
            st.write("- Tell a trusted friend, family member, or mental health professional")
            st.write("\nYou don't have to go through this alone. Help is available.")

        st.session_state.conversation_history.append({
            "role": "assistant",
            "content": "I've detected you might be in crisis. Please see the emergency resources above."
        })

    def run(self):
        self.initialize_session_state()

        if not st.session_state.user_info_collected:
            self.get_user_info()
        else:
            self.chat_interface()


# Run the chatbot
if __name__ == "__main__":
    bot = DepressionSupportChatbot()
    bot.run()