import requests

def export_excel_file(text:str):
    """
    Test if dag works on new structure

    Parameters
    ----------
    text : string
        string to test result.
    """
    dls = "https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/EXCEL_FILES/1_General/WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1.xlsx"
    resp = requests.get(dls)

    output = open('data/WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1.xlsx', 'wb')
    output.write(resp.content)
    output.close()
