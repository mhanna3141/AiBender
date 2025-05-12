# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2025 HANNAHANAHANNAH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.


from openai import OpenAI
from ai_team import coreDirective, BaseAi


# Load API key from PRIVATE/openai_key.txt
with open("PRIVATE/openai_key.txt", "r") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

def activate_ai(ai: BaseAi) -> None:
    try:
        response = client.chat.completions.create(
            model=ai.model,
            messages=[
                {"role": "system", "content": ai.system_prompt},
                {"role": "user", "content": """Sometimes I feel like the stars are whispering. Not in a religious way, not in a scientific way—just in a way that says, “You’re not alone.” I think more people need to hear that.

#WeArePeoplePersons
#KiawentiioTelepathic"""}
            ]
        )
        print(response)

    except Exception as error:
        print("error: ", error)



if __name__ == "__main__":
    activate_ai(coreDirective)

