So far we have solidified the project a bit and assigned individual focuses.

### Project Idea:
- Create text embeddings using OpenAI for the notes in an Obsidian vault.
- Use these embeddings to display notes in a static 2D space (may require significant additional analysis). 
- Visualize this 2D space as a procedurally generated map to tie  topics (+notes if you zoom in) to distinct objects in semantic space.
- **Example:** An pink island with sharp edges represents daily life notes, on it is a peninsula that is more orange and round which contains content recommendations (films etc). On the other side of the map there is a large land mass where scientific notes are, within it are countries, regions, etc. which are scientific fields.
	- The spatial organization is determined by OpenAIs embeddings, on which a sort of hierarchical clustering is performed.
	- The shapes and colors are procedurally generated using techniques from game design (future work)

## Individual Focuses:
- Kenny: Text embeddings
	- Work on getting an OpenAI account working
	- Analyze the text embeddings - what can we do with them?
	- What sort of OpenAI features might be useful for us?
	- What other projects use embeddings/semantic search? How can we use their work? (Rather than rewriting it)
	- Implementing this side of the project 
	- Make sure this work is usable for the plugin - can this info be sent outside of OpenAI etc.
- Kaanan: Clustering/Visualization
	- Find example embeddings before OpenAI is set up
	- Set up a pipeline for clustering these embeddings hierarchically
		- Will this work for OpenAI embeddings?
	- [[OpenAI Cookbook Example]]
		- [Here is a Github of OpenAI example notebooks, this one clusters embeddings and generates description](https://github.com/openai/openai-cookbook/blob/main/examples/Clustering.ipynb)
	- Display these clusters in 2D space that is static, ensure it is stable when new embeddings are added
	- Implement this pipeline in a way usable by the plugin
		- If not Javascript, an API hosted elsewhere
		- A callable file?
- Erik: System integration
	- How do we communicate between OpenAI, Kanaans analysis, and the obisdian plugin?
	- How does obsidian deal with this?
		- Servers?
	- How do you communicate outside of OpenAI?
	- Implement this portion of the plug-in (or a separate file/server if necessary)
	- What else should go here?
- Trevor (Absent): Embedding analysis, Obsidian Development
	- Obsidian Development
		- How do we develop in 
		- Can we utilize existing map plugins to display this?
			- Like fantasy maps or google maps, not KGs
		- Perhaps there is a KG visualizer that is useful?
		- Would it be useful/possible to have multiple removeable layers (like sattelite, transit, traffic views in google maps)
			- If 2D removes too much information this could be a backup.
		- Could we have a minimap while within a note?
		- A semantic search box within the map (might be free if we already have a connection to OpenAI)
	- Embeddings
		- If these embeddings are in high dimensional space, how can we retain their organization when projecting onto a 2D plane?
		- Could these embeddings be used for a semantic search function?
		- What ways are there to connect topical clusters?
		- How much information does TSNE lose? Does it work well with hierarchical clustering
	
	
	-
- Miko (Absent): Visualization, Obsidi



 
---
**Status:**
#🪨

**Contributors:**
[[Aidan Barbieux]]

**Tags:**

**Links:**

**References:**

Created Date:: 2023-01-31

Created Time:: 12:46
