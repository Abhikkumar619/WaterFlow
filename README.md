#Langchain Chain 
##Create_opeani_fn_runnable: 
This method allow to create runnable that use openAI function calling. Basically useful for cases where you need 
to dynamically call external functons based on the conversation context, such as retriving data or performing some 
computation.

create_openai_fn_runnable(functions, llm_model)


## RUNNABLE_PARALLEL:
in langchian runnable parallel, is useful when you wnat to perform several tasks simultaneously, such as 
running multiple models, performing different tasks, or wuerying multiple data sources.

