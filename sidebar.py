import streamlit as st

import database


def delete_db_button():
        db_get = st.button("Reset Database")

        if db_get:
            database.reset_database()


def display_list_of_documents():
    st.subheader("Documents available")
    documents_names = database.get_document_names()
    if documents_names:
        for doc_name in documents_names:
            col_doc_name, col_doc_include, col_del_button = st.columns([4,3,1]) #Collums layout
            with col_doc_name:
                st.write(doc_name)
            with col_doc_include:
                toggle_state = st.checkbox("Toggle", key=f"toggle_{doc_name}")
            with col_del_button:
                delete_doc_button = st.button("X")
                if delete_doc_button:
                    with st.spinner(f"Deleting {doc_name}"):
                        database.remove_document_from_db(doc_name)
                st.rerun()

def sidebar():

    with st.sidebar:
        st.set_page_config(page_title="RAG Question Answer")
        st.header("Rag Question Answer")
        uploaded_file= st.file_uploader("Upload PDF File for QnA", type=["pdf"], accept_multiple_files=True)

        process = st.button(
            "Process"
        )

        if uploaded_file and process:
            with st.spinner("Inserting the documents in the database...", show_time = True):
                for doc in uploaded_file:
                    normalize_uploaded_file_name = doc.name.translate(
                        str.maketrans({"-":"_", ".": "_", " ":"_"})
                    )
                    all_splits = database.process_document(doc)
                    database.add_to_vector_collection(all_splits, normalize_uploaded_file_name, doc.name)

        display_list_of_documents()
        delete_db_button()

