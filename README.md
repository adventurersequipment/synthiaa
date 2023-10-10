# synthiaa
Creating an embodied agent for an MMORPG that integrates various elements like visual perception, decision-making, and self-awareness.

Phase 1: Infrastructure and Basic Interface
Game API Interface / Simulated User Input: Develop the most basic interface layer to interact with Everquest. If the game has an API, use it; otherwise, build a program to simulate mouse and keyboard inputs.
Data Collection: Implement a way to collect game state information, either via the game's API or by reading it from the display.
Memory Buffer: Start building the memory buffer for storing game states and actions which will be utilized in later phases.

Phase 2: Visual Perception
Object Detection: Integrate MobileNet or a similar lightweight visual perception model for basic object identification.
Preprocessing Module: Implement the module that prepares the visual data for object detection.

Phase 3: Natural Language Understanding
Contextual Understanding: Integrate GPT-4 for basic narrative structuring and context interpretation.
Task-Specific LLMs: Design language models specialized in game-specific tasks.

Phase 4: Decision Making and Self Model
Reinforcement Learning Module: Implement a basic RL module for decision-making based on the game mechanics.
Executive Function: Introduce the higher-level decision-making layer using GPT-4's narrative capabilities.
Self-Referential LLM: Integrate the self-referential large language model to start building a sense of self.

Phase 5: Active Learning and Feedback
Data Augmentation: Utilize the language models for real-time training data augmentation.
Feedback Mechanism: Implement real-time feedback loops for adaptivity and optimization.
