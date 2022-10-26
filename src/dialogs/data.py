

async def get(dialog_manager, **kwargs):
    data = dialog_manager.current_context().dialog_data
    current_state = dialog_manager.current_context().state

    answer_from_data = data.get("answers", {}).get(current_state.name, "")

    result = {
        "question": current_state.get_question(answer_from_data),
        "answer": answer_from_data,
        "options": [(opt, str(i)) for i, opt in enumerate(current_state.options)],
    }
    return result
