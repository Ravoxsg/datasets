package corgis.graduates.domain;

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
public class Gender {
	
    // The estimated number of women awarded degrees in this major during this year.
    private Integer males;
    // The estimated number of women awarded degrees in this major during this year.
    private Integer females;
    
    
    /*
     * @return 
     */
    public Integer getMales() {
        return this.males;
    }
    
    
    
    /*
     * @return 
     */
    public Integer getFemales() {
        return this.females;
    }
    
    
    
	
	/**
	 * Creates a string based representation of this Gender.
	
	 * @return String
	 */
	public String toString() {
		return "Gender[" +males+", "+females+"]";
	}
	
	/**
	 * Internal constructor to create a Gender from a  representation.
	 * @param json_data The raw json data that will be parsed.
	 */
    public Gender(JSONObject json_data) {
        try {// Males
            this.males = ((Number)json_data.get("Males")).intValue();// Females
            this.females = ((Number)json_data.get("Females")).intValue();
        } catch (NullPointerException e) {
    		System.err.println("Could not convert the response to a Gender; a field was missing.");
    		e.printStackTrace();
    	} catch (ClassCastException e) {
    		System.err.println("Could not convert the response to a Gender; a field had the wrong structure.");
    		e.printStackTrace();
        }
	}	
}