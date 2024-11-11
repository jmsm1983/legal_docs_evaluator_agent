from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("-ADVANCED RAG USED TO EVALUATE LEGAL DOCUMENTS")

    question1="""What are the conditions that need to be satisfied for Buyer to purchase the Assets and assume the liabilities in this agreement?"""
    question2="""Who is James Bond"""
    question3="""How would you rate this clause from 1 -10 according the level of risks: From and after the Closing Date, to the extent provided in this Article 8, Seller shall indemnify, defend and hold harmless Buyer and its Affiliates and their respective officers, directors, employees, agents, successors and assigns from and against any claims, suits or proceedings and any damages or liability therefrom or settlement thereof (including reasonable fees of attorneys and related costs) to the extent arising out of or related to (a) any breach of any representation, warranty, covenant or agreement of Seller contained herein and (b) any Excluded Liability"""
    question4="""
    
                Evaluate the following scenarios against Dow Jones code of conduct and say if they are ok or against it.
        
                1.An employee in the editorial department has access to unpublished information about a company about to be featured in an upcoming article. They share this information with a family member, who subsequently uses it to make an investment decision before the article is published
                2.An employee with authority to approve contracts chooses a supplier owned by a close family member without disclosing the relationship to Dow Jones.
                3.An employee uses company funds and resources, such as printers and work time, to print and distribute flyers for a personal business they are running on the side.
                4.A Dow Jones sales manager accepts tickets to a luxury event from a client in exchange for prioritizing their advertising content.
                5.To meet quarterly goals, a financial manager manipulates reporting data to artificially inflate earnings. This results in inaccurate disclosures in the company’s filings.
                6.A senior editor at Dow Jones publicly endorses and actively campaigns for a political candidate in their community.
                7.An employee who frequently handles sensitive business information about Dow Jones’ partnerships buys stock in a company before the public announcement of a new contract. They then sell the stock immediately after the partnership is publicized, making a quick profit.
                8.An employee raises a concern with management regarding a colleague’s misuse of confidential information. The employee’s supervisor begins excluding them from team projects and provides a negative performance review as a result.
                9.During a hiring process, a manager excludes candidates based on their age or marital status.
                10.A Dow Jones facility supervisor disregards a health and safety hazard in the workplace to cut costs, despite the potential harm to employees.               
               """

    question5="""
    This clause is part of an NDA. Please review the clause to determine if it aligns with our acceptability standards.
    The Receiving Party may use Confidential Information at its discretion for purposes it deems necessary, including, but not limited to, general business development, marketing analysis, or unrelated internal projects. Confidential Information may be shared freely with external consultants, partners, and affiliates, with no specific limitations or confidentiality requirements for those third parties. Confidential Information shall remain confidential for an indefinite period, except in cases where the Receiving Party deems disclosure to be beneficial or necessary. The Receiving Party reserves the right to disclose Confidential Information without prior notice to the Disclosing Party if required by internal business processes.
    . If it does not, rewrite the clause to fully comply with our predefined acceptability policies. """


    question6="""
Article 3 Closing
3.1	 	
Closing Date. The closing of the transactions contemplated hereby ("Closing") shall be held in Beijing, on the Closing Date, and shall be effective as of 12:01a.m. local time on the Closing Date. All matters at the Closing shall be considered to take place simultaneously.
3.2	 	
Closing Documents. The Seller and the Purchaser shall deliver to each other at the Closing the Closing Documents. The Seller and Management Shareholder further agree that at or subsequent to the Closing, upon the written request of the Purchaser, it will promptly execute and deliver or cause to be promptly executed and delivered, by itself or the Operator, any further assignment, instruments of transfer and bills of sale or conveyances reasonably necessary or desirable to vest fully in the Purchaser all of the Seller's right, title and interest in and to the Assets.
Article 4 Seller's and Management Shareholder's Representations and Warranties
The Seller and the Management Shareholder each jointly and severally represent and warrant as follows and undertake the joint and several liabilities:
4.1	 	
Ownership of Assets. Based on the Offshore-ATA Closing, Appendix II sets forth all of the assets of the Operator transferred to the Seller by the Operator. The Seller has good and marketable title to the Assets, including to all underlying intellectual property rights, free of any mortgages, pledges or encumbrances or other security interests, and is entitled to transfer the Assets to the Purchaser, provided that the Pharos System shall be disposed of in accordance with Appendix IV.
4.2	 	
Registration of Assets. Based on the Offshore-ATA Closing, the Operator and the Management Shareholder have undertaken and maintained at their sole expense all registrations of the intellectual property rights and other relevant rights of the Assets that are necessary to protect them as proprietary property under applicable Laws, and the existence, or their registration or use of such intellectual property does not infringe on the rights of others, provided that the Pharos System shall be disposed of in accordance with Appendix IV.

    can you please rate each clause of the document from 1 to 10 according to the level of risk 10: Very high, 1: very low
    """

    answer= app.invoke(input={"question": question6})
    print (answer)






