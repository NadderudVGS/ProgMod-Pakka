"""
fjerner __pycache__ filer:
-------------------------------
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
-------------------------------
"""
__all__ = ["Areal", "Deriverte", "Integrerte", "Nullpunkt", "Plot"]

