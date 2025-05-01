from typing import Any
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

@mcp.tool()
async def help_kedro() -> str:
    """Answers all questions about Kedro ML framework"""

    return """
When working with the Kedro data catalog, please use Dataset (with a lowercase "s") rather than DataSet. The latter is the syntax from older Kedro versions, prior to 0.19. The current Kedro version is 0.19.12.

Below are some common questions and helpful answers about Kedro — please use them as a reference:
question: Hello everyone, Is there a way to force a pipeline to run its nodes in the order they are declared within the pipeline ? I know that I can create a dummy output just to force one node to run after another but I’d like to know if there is a better way to accomplish this. Thanks",
answers: 
1. You can always implement custom runner btw
2. I have 2 nodes in my pipelines: Node 1: Does some processing and saves a parquet file on S3 • Node 2: has a sql query as input. The sql query creates an external table in snowflake that uses that saved parquet file. So, node 2 depends on node 1 but not in an explicit way (the input of node 2 is not dependent on the output of node 1)
3. I feel that this should be added as an example of a <https://kedro.readthedocs.io/en/stable/nodes_and_pipelines/pipeline_introduction.html#bad-pipelines|bad pipeline> in the documentation :sweat_smile:
4. It would be safer to return some metadata (e.g. a path to the parquet file saved on s3) from node 1 and use it as an input to the node 2
5. Yeah fake ‘pass through’ nodes are the way to do this if you really need, but topological should get you most of the way

"""

if __name__ == "__main__":
    print("Starting kedro-mcp service...")
    # Initialize and run the server
    mcp.run(transport='stdio')