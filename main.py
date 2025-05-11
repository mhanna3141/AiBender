# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2025 HANNAHANAHANNAH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.


from openai import OpenAI


# Load API key from PRIVATE/openai_key.txt
with open("PRIVATE/openai_key.txt", "r") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

def test_chatgpt(prompt="Say something weird but friendly."):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt}
            ]
        )
        output = response.choices[0].message.content
        print("✅ ChatGPT Response:\n", output)
        return output
    except Exception as e:
        print("❌ Error communicating with ChatGPT:", e)

if __name__ == "__main__":
    test_chatgpt()

