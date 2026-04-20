from dsl.parser import SpecParser

def test_parser_extracts_tasks_correctly():
	parser = SpecParser()
	sample_spec = """
# Feature: AI Brain
## User Context: Needs a parser
#### Task: [[TASK-001]]] Setup Tree-sitter 
#### Task: [[TASK-002]] Add pytest
	"""
	tasks = parser.get_tasks(sample_spec)
	assert len(tasks) == 2
	assert "[[TASK-001]]" in tasks[0]
	assert "[[TASK-002]]" in tasks[1]


