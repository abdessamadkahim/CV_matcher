from app.schemas import JobDescriptionData,ResumeData
from app.services.matcher import match_skills
def test_match_skills():
  resume=ResumeData(
    skills=["Python","SQL","Power BI","Machine Learning","Statistiques"]
  )
  job=JobDescriptionData(
    required_skills=["Python","SQL","Power BI","Excel","Statistiques"]
  )
  result=match_skills(resume,job)
  print("\n========== MATCHING ==========")
  print("Compétences communes :", result["matched_skills"])
  print("Compétences manquantes :", result["missing_skills"])
  print("Score :", result["score"])
  
  assert result["score"]==0.8
  assert "python" in result["matched_skills"]
  assert "excel" in result["missing_skills"]
  
