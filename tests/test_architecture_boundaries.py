from pathlib import Path


def test_core_modules_stay_below_entropy_budget():
    root = Path(__file__).resolve().parents[1]
    budgets = {
        "deepcode/core/runtime.py": 950,
        "deepcode/core/runtime_events.py": 90,
        "deepcode/core/runtime_consumers.py": 90,
        "deepcode/core/artifacts.py": 130,
        "deepcode/core/task_state.py": 140,
        "deepcode/core/todo_ledger.py": 120,
        "deepcode/core/worker_manager.py": 220,
        "deepcode/core/context_manager.py": 420,
        "deepcode/core/context_usage.py": 120,
        "deepcode/core/compact.py": 180,
        "deepcode/core/engine.py": 470,
        "deepcode/core/model_errors.py": 100,
        "deepcode/core/permissions.py": 140,
        "deepcode/core/tool_policy.py": 90,
        "deepcode/core/plan_mode.py": 140,
        "deepcode/core/tool_executor.py": 181,
        "deepcode/core/tool_profiles.py": 80,
        "deepcode/core/turn_history.py": 250,
        "deepcode/features/skills.py": 220,
        "deepcode/features/skills_bundled.py": 120,
        "deepcode/features/skills_runtime.py": 140,
        "deepcode/tools/registry.py": 360,
        "deepcode/tools/todos.py": 80,
        "deepcode/tools/agents.py": 90,
    }

    for relative_path, max_lines in budgets.items():
        line_count = len((root / relative_path).read_text(encoding="utf-8").splitlines())
        assert line_count <= max_lines, f"{relative_path} has {line_count} lines, budget is {max_lines}"
