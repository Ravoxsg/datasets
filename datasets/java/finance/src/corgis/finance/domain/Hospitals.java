package corgis.finance.domain;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;


/**
 * 
 */
public class Hospitals {
	
    private Integer ownHospitalsTotalExpenditure;
    private Integer hospitalOtherTotalExpenditure;
    private Integer hospitalsTotalExpenditure;
    private Integer hospitalsTotalIntergovernmental;
    private Integer hospitalsTotalEquipmentAndLand;
    private Integer hospitalsTotalConstruction;
    private Integer hospitalsTotalCurrent;
    private Integer hospitalOtherIntergovernmental;
    
    
    /*
     * @return 
     */
    public Integer getOwnHospitalsTotalExpenditure() {
        return this.ownHospitalsTotalExpenditure;
    }
    
    
    
    /*
     * @return 
     */
    public Integer getHospitalOtherTotalExpenditure() {
        return this.hospitalOtherTotalExpenditure;
    }
    
    
    
    /*
     * @return 
     */
    public Integer getHospitalsTotalExpenditure() {
        return this.hospitalsTotalExpenditure;
    }
    
    
    
    /*
     * @return 
     */
    public Integer getHospitalsTotalIntergovernmental() {
        return this.hospitalsTotalIntergovernmental;
    }
    
    
    
    /*
     * @return 
     */
    public Integer getHospitalsTotalEquipmentAndLand() {
        return this.hospitalsTotalEquipmentAndLand;
    }
    
    
    
    /*
     * @return 
     */
    public Integer getHospitalsTotalConstruction() {
        return this.hospitalsTotalConstruction;
    }
    
    
    
    /*
     * @return 
     */
    public Integer getHospitalsTotalCurrent() {
        return this.hospitalsTotalCurrent;
    }
    
    
    
    /*
     * @return 
     */
    public Integer getHospitalOtherIntergovernmental() {
        return this.hospitalOtherIntergovernmental;
    }
    
    
    
	
	/**
	 * Creates a string based representation of this Hospitals.
	
	 * @return String
	 */
	public String toString() {
		return "Hospitals[" +ownHospitalsTotalExpenditure+", "+hospitalOtherTotalExpenditure+", "+hospitalsTotalExpenditure+", "+hospitalsTotalIntergovernmental+", "+hospitalsTotalEquipmentAndLand+", "+hospitalsTotalConstruction+", "+hospitalsTotalCurrent+", "+hospitalOtherIntergovernmental+"]";
	}
	
	/**
	 * Internal constructor to create a Hospitals from a  representation.
	 * @param json_data The raw json data that will be parsed.
	 */
    public Hospitals(JSONObject json_data) {
        try {// Own Hospitals Total Expenditure
            this.ownHospitalsTotalExpenditure = ((Number)json_data.get("Own Hospitals Total Expenditure")).intValue();// Hospital-Other Total Expenditure
            this.hospitalOtherTotalExpenditure = ((Number)json_data.get("Hospital-Other Total Expenditure")).intValue();// Hospitals Total Expenditure
            this.hospitalsTotalExpenditure = ((Number)json_data.get("Hospitals Total Expenditure")).intValue();// Hospitals Total Intergovernmental
            this.hospitalsTotalIntergovernmental = ((Number)json_data.get("Hospitals Total Intergovernmental")).intValue();// Hospitals Total Equipment and land
            this.hospitalsTotalEquipmentAndLand = ((Number)json_data.get("Hospitals Total Equipment and land")).intValue();// Hospitals Total Construction
            this.hospitalsTotalConstruction = ((Number)json_data.get("Hospitals Total Construction")).intValue();// Hospitals Total Current
            this.hospitalsTotalCurrent = ((Number)json_data.get("Hospitals Total Current")).intValue();// Hospital-Other Intergovernmental
            this.hospitalOtherIntergovernmental = ((Number)json_data.get("Hospital-Other Intergovernmental")).intValue();
        } catch (NullPointerException e) {
    		System.err.println("Could not convert the response to a Hospitals; a field was missing.");
    		e.printStackTrace();
    	} catch (ClassCastException e) {
    		System.err.println("Could not convert the response to a Hospitals; a field had the wrong structure.");
    		e.printStackTrace();
        }
	}	
}