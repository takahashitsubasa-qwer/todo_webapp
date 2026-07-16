# source .venv/bin/activate
#streamlit run streamlit.py

import streamlit as st
import random
import requests
import json
import pandas as pd

st.title('todo')
tab1, tab2 = st.tabs(["put_todo", "containered_todo"])
with tab1:
    #post_todo
    with st.form("post"):
        st.header("add_new_todo")
        #content
        title_content: str = st.text_input('content')
        #priority
        options=["high","middle","low"]
        priority = st.pills("priority",options)

        data = {
            "title_content": title_content,
            "priority": priority,
        }
        submit_button = st.form_submit_button(label='commit')

    if submit_button:
        url = 'http://127.0.0.1:8000/todos'
        res = requests.post(
            url,
            json = data
        )

    #space
    st.space("medium")

    #todolist_data
    url = 'http://127.0.0.1:8000/todos'
    res = requests.get(url)
    df =pd.DataFrame(res.json())
    res_json=res.json()
    ##data no kakuninn##
    # st.write(res_json)

    #todo_list
    for todo in res_json:
        if todo["done"]==0:
            with st.container(border=True):
                st.write(f'□ {todo["title_content"]}')
                st.write(f'優先度：{todo["priority"]}')
                col1, col2, col3 = st.columns(3)
                #completion button
                with col1:
                    completion = st.button("completion", width="stretch",key=(f"completion_{todo["todo_id"]}"))
                    if completion:
                        url = f"http://127.0.0.1:8000/todos/{todo["todo_id"]}/done"
                        response = requests.patch(url)
                        st.rerun()
                #edit button
                with col2:
                    edit = st.button("edit", width="stretch",key=(f"edit_{todo["todo_id"]}"))
                    if edit:
                        @st.dialog("todo_edit")
                        def todo_edit_define(content):
                            st.write(list(content)[0])
                            title_content: str = st.text_input('content')
                            #priority
                            options=["high","middle","low"]
                            priority = st.pills("priority",options)

                            edit_data = {
                                "title_content": title_content,
                                "priority": priority
                            }

                            edit_button = st.button(label='edit')
                            if edit_button:
                                url_edit = f'http://127.0.0.1:8000/todos/{todo["todo_id"]}'
                                response = requests.put(url_edit,json=edit_data)
                                st.rerun()
                        todo_edit_define(todo["title_content"])
                #delete button
                with col3:
                    delete = st.button("delete", width="stretch",key=(f"delete_{todo["todo_id"]}"))
                    if delete:
                        url_delete = f'http://127.0.0.1:8000/todos/{todo["todo_id"]}'
                        response = requests.delete(url_delete)
                        st.write(response.status_code)
                        st.rerun()
        


with tab2: 
    for todo in res_json:
        if todo["done"]==1:
            with st.container(border=True):
                st.write(f"□ {todo["title_content"]}")
                st.write(f"優先度：{todo["priority"]}")

