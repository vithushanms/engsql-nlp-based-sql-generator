'''
Filename: gpt.py
Created Date: Friday, April 7th 2023, 1:59:59 am
Author: Vithushan Sylvester

Copyright (c) 2023 Vithushan Sylvester
'''

import openai

#class definition of custom GPT stucture to store examples
class GPT:
    def __init__(self, engine, temperature, max_tokens):
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.examples = []

    #add examples into the GPT structure to give more context to the model
    def add_example(self, example):
        self.examples.append(example)
        
    #get the response from the openai api
    def submit_request(self, prompt):
        prompt_with_examples = self._build_prompt_with_examples(prompt)

        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt_with_examples,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            n=1,
            stop=None,
            echo=False,
        )

        return response

    def _build_prompt_with_examples(self, prompt):
        prompt_with_examples = ""
        for example in self.examples:
            prompt_with_examples += f"Q: {example.input}\nA: {example.output}\n"
        prompt_with_examples += f"Q: {prompt}\n"

        return prompt_with_examples

#data structure to store the input and output of the examples
class Example:
    def __init__(self, input, output):
        self.input = input
        self.output = output
