from tree_sitter_languages import get_language, get_parser

class SpecParser:
	def __init__(self):
		self.lang = get_language("markdown")
		self.parser = get_parser("markdown")
		self.query = self.lang.query("""

			(atx_heading
				(atx_h4_marker)
					(heading_content) (_) @task_text
			)
		""")
		self.query = self.lang.query("""

			(atx_heading
				(atx_h4_marker)
					(_) @task_text)
		""")
	def get_tasks(self, text: str):
		tree = self.parser.parse(bytes(text, "UTF-8"))
		captures = self.query.captures(tree.root_node)
		tasks = []
		for node, _ in captures:
			tasks.append(node.text.decode("UTF-8").strip())
		return tasks
